# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T18:07:20.732936+00:00`
- Correlation status: `ready`
- Asset price records: `572`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0106` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.5719` n `12`; crypto_alt avg `0.6859` n `228`; crypto_major avg `0.4365` n `8`; equity avg `0.3518` n `65`; fx avg `-0.0285` n `5`; index avg `0.3014` n `23`; metal avg `0.2906` n `18`; unknown avg `0.0917` n `365`
- 1h: commodity avg `-0.3839` n `12`; crypto_alt avg `0.7208` n `228`; crypto_major avg `0.3743` n `8`; equity avg `0.2926` n `65`; fx avg `-0.0355` n `5`; index avg `0.1103` n `23`; metal avg `-0.1327` n `18`; unknown avg `0.0845` n `365`
- 4h: commodity avg `1.8256` n `12`; crypto_alt avg `0.5732` n `228`; crypto_major avg `-0.185` n `8`; equity avg `-1.0231` n `65`; fx avg `0.0326` n `5`; index avg `-0.3656` n `23`; metal avg `-1.0046` n `18`; unknown avg `-0.1732` n `365`
- 24h: commodity avg `0.122` n `12`; crypto_alt avg `1.3954` n `228`; crypto_major avg `-1.4188` n `8`; equity avg `-0.6153` n `65`; fx avg `0.1653` n `5`; index avg `-0.4169` n `23`; metal avg `0.7438` n `18`; unknown avg `0.0901` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `568`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `568`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `568`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `568`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0967`, n `564`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `564`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0917`, n `564`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `564`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0883`, n `564`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0747`, n `564`, weak_sample_signal
