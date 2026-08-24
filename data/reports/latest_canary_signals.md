# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T13:34:54.009429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0735` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `-0.9021` n `231`; crypto_major avg `-0.7769` n `8`; equity avg `-0.885` n `122`; fx avg `0.0024` n `6`; index avg `-0.1073` n `25`; metal avg `0.08` n `20`; unknown avg `1.5832` n `793`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.4285` n `231`; crypto_major avg `-0.32` n `8`; equity avg `-0.9216` n `122`; fx avg `0.0306` n `6`; index avg `-0.1107` n `25`; metal avg `0.1729` n `20`; unknown avg `0.4421` n `793`
- 4h: commodity avg `0.2271` n `12`; crypto_alt avg `0.3745` n `231`; crypto_major avg `0.949` n `8`; equity avg `-1.1245` n `122`; fx avg `0.0479` n `6`; index avg `-0.1488` n `25`; metal avg `0.3177` n `20`; unknown avg `0.9045` n `793`
- 24h: commodity avg `0.0397` n `12`; crypto_alt avg `-0.2609` n `231`; crypto_major avg `0.0736` n `8`; equity avg `-2.5389` n `122`; fx avg `-0.1133` n `6`; index avg `-0.2786` n `25`; metal avg `0.3659` n `20`; unknown avg `3.8127` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
