# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T21:52:20.399698+00:00`
- Correlation status: `ready`
- Asset price records: `587`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1988` n `12`; crypto_alt avg `0.0143` n `228`; crypto_major avg `-0.0202` n `8`; equity avg `-0.3039` n `65`; fx avg `-0.0152` n `5`; index avg `-0.061` n `23`; metal avg `0.0153` n `18`; unknown avg `0.4195` n `365`
- 1h: commodity avg `0.2347` n `12`; crypto_alt avg `0.054` n `228`; crypto_major avg `-0.0662` n `8`; equity avg `-0.8242` n `65`; fx avg `-0.0412` n `5`; index avg `-0.1893` n `23`; metal avg `-0.4453` n `18`; unknown avg `-0.0962` n `365`
- 4h: commodity avg `0.529` n `12`; crypto_alt avg `0.5912` n `228`; crypto_major avg `0.0216` n `8`; equity avg `-0.6456` n `65`; fx avg `-0.0578` n `5`; index avg `-0.1225` n `23`; metal avg `-0.5773` n `18`; unknown avg `-0.4713` n `365`
- 24h: commodity avg `0.8699` n `12`; crypto_alt avg `0.6249` n `228`; crypto_major avg `-2.1143` n `8`; equity avg `-1.5181` n `65`; fx avg `0.1454` n `5`; index avg `-0.983` n `23`; metal avg `-0.3847` n `18`; unknown avg `-0.4574` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1399`, n `583`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1133`, n `583`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `583`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `583`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `579`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `579`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `579`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0872`, n `579`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0822`, n `579`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.082`, n `579`, weak_sample_signal
