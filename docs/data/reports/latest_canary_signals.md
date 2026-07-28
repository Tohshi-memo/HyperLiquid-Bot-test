# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T13:52:30.860364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.909` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.7259` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `-0.0388` n `230`; crypto_major avg `0.0718` n `8`; equity avg `-0.7601` n `102`; fx avg `0.0143` n `6`; index avg `-0.0374` n `25`; metal avg `0.0172` n `20`; unknown avg `0.0272` n `774`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.6114` n `230`; crypto_major avg `-0.4442` n `8`; equity avg `-2.1701` n `102`; fx avg `0.0344` n `6`; index avg `-0.13` n `25`; metal avg `-0.1692` n `20`; unknown avg `-0.0078` n `774`
- 4h: commodity avg `0.1075` n `12`; crypto_alt avg `-0.6033` n `230`; crypto_major avg `-0.6422` n `8`; equity avg `-2.5512` n `102`; fx avg `0.03` n `6`; index avg `-0.1074` n `25`; metal avg `-0.0727` n `20`; unknown avg `0.0898` n `774`
- 24h: commodity avg `-0.7158` n `12`; crypto_alt avg `-4.1511` n `230`; crypto_major avg `-4.3241` n `8`; equity avg `-5.8572` n `102`; fx avg `-0.1354` n `6`; index avg `-0.8011` n `25`; metal avg `-0.6368` n `20`; unknown avg `1225.153` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
