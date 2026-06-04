# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T01:07:21.074594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0686` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1129` n `12`; crypto_alt avg `0.1139` n `228`; crypto_major avg `0.2875` n `8`; equity avg `0.1216` n `73`; fx avg `0.0036` n `6`; index avg `0.0411` n `23`; metal avg `0.1318` n `18`; unknown avg `1.2619` n `419`
- 1h: commodity avg `-0.0895` n `12`; crypto_alt avg `-1.1881` n `228`; crypto_major avg `-0.9161` n `8`; equity avg `0.379` n `73`; fx avg `-0.0265` n `6`; index avg `0.1525` n `23`; metal avg `0.1584` n `18`; unknown avg `0.7571` n `419`
- 4h: commodity avg `-0.7097` n `12`; crypto_alt avg `-0.8863` n `228`; crypto_major avg `-0.9578` n `8`; equity avg `-0.4571` n `73`; fx avg `-0.0548` n `6`; index avg `-0.1698` n `23`; metal avg `0.4947` n `18`; unknown avg `-0.1286` n `419`
- 24h: commodity avg `0.1173` n `12`; crypto_alt avg `0.1538` n `228`; crypto_major avg `-2.2566` n `8`; equity avg `-3.2457` n `72`; fx avg `-0.0123` n `6`; index avg `-1.1977` n `23`; metal avg `-1.3955` n `18`; unknown avg `1.5785` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
