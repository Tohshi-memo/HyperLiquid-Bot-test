# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T20:08:10.466978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4251` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0786` n `12`; crypto_alt avg `0.0041` n `228`; crypto_major avg `-0.0871` n `8`; equity avg `0.0417` n `74`; fx avg `0.0001` n `6`; index avg `0.1104` n `23`; metal avg `-0.042` n `18`; unknown avg `0.0804` n `556`
- 1h: commodity avg `-0.8164` n `12`; crypto_alt avg `0.2324` n `228`; crypto_major avg `0.3205` n `8`; equity avg `0.9127` n `74`; fx avg `-0.0029` n `6`; index avg `0.4698` n `23`; metal avg `0.7078` n `18`; unknown avg `-0.2538` n `556`
- 4h: commodity avg `-1.7037` n `12`; crypto_alt avg `1.0378` n `228`; crypto_major avg `1.7214` n `8`; equity avg `2.1922` n `74`; fx avg `0.06` n `6`; index avg `1.3015` n `23`; metal avg `2.5845` n `18`; unknown avg `0.2261` n `556`
- 24h: commodity avg `-2.2046` n `12`; crypto_alt avg `4.0395` n `228`; crypto_major avg `4.0422` n `8`; equity avg `4.0509` n `74`; fx avg `0.0273` n `6`; index avg `2.4198` n `23`; metal avg `3.4926` n `18`; unknown avg `2.3941` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
