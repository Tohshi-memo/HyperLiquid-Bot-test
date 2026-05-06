# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T10:52:21.801322+00:00`
- Correlation status: `ready`
- Asset price records: `447`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.1728` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.4869` n `7`; crypto_alt avg `0.0621` n `223`; crypto_major avg `0.0027` n `7`; equity avg `0.111` n `47`; fx avg `-0.0403` n `4`; index avg `-0.1091` n `6`; metal avg `0.1421` n `7`; unknown avg `-0.0288` n `313`
- 1h: commodity avg `-1.055` n `7`; crypto_alt avg `0.2233` n `223`; crypto_major avg `0.206` n `7`; equity avg `0.2847` n `47`; fx avg `-0.1091` n `4`; index avg `0.1721` n `6`; metal avg `0.5463` n `7`; unknown avg `-0.1877` n `313`
- 4h: commodity avg `-2.8195` n `7`; crypto_alt avg `1.7551` n `223`; crypto_major avg `1.3533` n `7`; equity avg `1.1617` n `47`; fx avg `-0.202` n `4`; index avg `0.8296` n `6`; metal avg `1.5357` n `7`; unknown avg `0.6002` n `313`
- 24h: commodity avg `-4.0831` n `7`; crypto_alt avg `4.0443` n `223`; crypto_major avg `3.0164` n `7`; equity avg `3.7394` n `47`; fx avg `-0.6757` n `4`; index avg `2.9749` n `6`; metal avg `3.4603` n `7`; unknown avg `1.8861` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.168`, n `443`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1619`, n `443`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1506`, n `443`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `443`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `443`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `443`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1148`, n `439`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `439`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0971`, n `439`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `439`, weak_sample_signal
