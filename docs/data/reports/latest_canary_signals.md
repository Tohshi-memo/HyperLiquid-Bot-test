# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T14:07:28.567562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.309` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.4953` n `231`; crypto_major avg `0.5032` n `8`; equity avg `0.2604` n `122`; fx avg `-0.0059` n `6`; index avg `0.017` n `25`; metal avg `0.0498` n `20`; unknown avg `0.0245` n `793`
- 1h: commodity avg `-0.1685` n `12`; crypto_alt avg `-0.9753` n `231`; crypto_major avg `-0.9424` n `8`; equity avg `-1.4221` n `122`; fx avg `-0.0003` n `6`; index avg `-0.2064` n `25`; metal avg `-0.0249` n `20`; unknown avg `-0.0315` n `793`
- 4h: commodity avg `0.1194` n `12`; crypto_alt avg `0.0971` n `231`; crypto_major avg `0.5888` n `8`; equity avg `-1.7202` n `122`; fx avg `0.0051` n `6`; index avg `-0.2618` n `25`; metal avg `0.1587` n `20`; unknown avg `0.7742` n `793`
- 24h: commodity avg `-0.0871` n `12`; crypto_alt avg `-0.6302` n `231`; crypto_major avg `-0.196` n `8`; equity avg `-3.0585` n `122`; fx avg `-0.1178` n `6`; index avg `-0.3792` n `25`; metal avg `0.2886` n `20`; unknown avg `3.7584` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
