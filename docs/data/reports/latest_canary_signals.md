# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T14:22:31.490707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4535` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0523` n `12`; crypto_alt avg `0.6047` n `231`; crypto_major avg `0.6291` n `8`; equity avg `0.2626` n `122`; fx avg `0.0188` n `6`; index avg `0.0407` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.054` n `793`
- 1h: commodity avg `-0.169` n `12`; crypto_alt avg `-0.4687` n `231`; crypto_major avg `-0.3711` n `8`; equity avg `-1.1486` n `122`; fx avg `0.0107` n `6`; index avg `-0.1729` n `25`; metal avg `0.0049` n `20`; unknown avg `1.0001` n `793`
- 4h: commodity avg `0.087` n `12`; crypto_alt avg `0.6769` n `231`; crypto_major avg `1.1095` n `8`; equity avg `-1.344` n `122`; fx avg `0.0276` n `6`; index avg `-0.2084` n `25`; metal avg `0.1706` n `20`; unknown avg `1.9453` n `793`
- 24h: commodity avg `-0.127` n `12`; crypto_alt avg `-0.1842` n `231`; crypto_major avg `0.1596` n `8`; equity avg `-2.8251` n `122`; fx avg `-0.0963` n `6`; index avg `-0.3485` n `25`; metal avg `0.3058` n `20`; unknown avg `3.7525` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
