# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T16:52:28.578644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8149` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0321` n `13`; crypto_alt avg `0.3027` n `239`; crypto_major avg `0.1638` n `8`; equity avg `0.0346` n `168`; fx avg `0.0135` n `6`; index avg `0.0` n `27`; metal avg `0.0261` n `20`; unknown avg `-0.0991` n `1266`
- 1h: commodity avg `-0.1241` n `13`; crypto_alt avg `-0.0412` n `239`; crypto_major avg `-0.2317` n `8`; equity avg `-0.6014` n `168`; fx avg `0.0319` n `6`; index avg `-0.0602` n `27`; metal avg `-0.0123` n `20`; unknown avg `5.247` n `1258`
- 4h: commodity avg `0.242` n `13`; crypto_alt avg `-0.2111` n `239`; crypto_major avg `-0.37` n `8`; equity avg `-2.1849` n `168`; fx avg `0.0389` n `6`; index avg `-0.2207` n `27`; metal avg `-0.6566` n `20`; unknown avg `364.3424` n `1241`
- 24h: commodity avg `0.2848` n `13`; crypto_alt avg `-1.1165` n `239`; crypto_major avg `-2.0589` n `8`; equity avg `-5.2715` n `168`; fx avg `-0.0287` n `6`; index avg `-0.5524` n `27`; metal avg `-1.0952` n `20`; unknown avg `615.6586` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
