# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T23:52:13.828507+00:00`
- Correlation status: `ready`
- Asset price records: `595`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1209` n `12`; crypto_alt avg `0.0747` n `228`; crypto_major avg `0.0867` n `8`; equity avg `0.0525` n `65`; fx avg `0.0057` n `5`; index avg `0.0491` n `23`; metal avg `0.1195` n `18`; unknown avg `0.0833` n `365`
- 1h: commodity avg `-0.0687` n `12`; crypto_alt avg `0.4796` n `228`; crypto_major avg `0.2637` n `8`; equity avg `0.467` n `65`; fx avg `-0.0045` n `5`; index avg `0.2062` n `23`; metal avg `0.4608` n `18`; unknown avg `0.0796` n `365`
- 4h: commodity avg `0.1746` n `12`; crypto_alt avg `0.25` n `228`; crypto_major avg `-0.0175` n `8`; equity avg `-0.0538` n `65`; fx avg `-0.0518` n `5`; index avg `0.0496` n `23`; metal avg `-0.0903` n `18`; unknown avg `-0.338` n `365`
- 24h: commodity avg `0.7131` n `12`; crypto_alt avg `1.4502` n `228`; crypto_major avg `-1.7461` n `8`; equity avg `-1.3931` n `65`; fx avg `0.1368` n `5`; index avg `-0.799` n `23`; metal avg `-0.085` n `18`; unknown avg `-0.4799` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.138`, n `591`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `591`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `591`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `591`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `587`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `587`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `587`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0793`, n `587`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.079`, n `587`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0747`, n `587`, weak_sample_signal
