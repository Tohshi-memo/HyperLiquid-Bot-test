# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T08:52:21.778954+00:00`
- Correlation status: `ready`
- Asset price records: `535`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.32` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0945` n `228`; crypto_major avg `0.0297` n `8`; equity avg `-0.0969` n `65`; fx avg `0.0325` n `4`; index avg `-0.0227` n `23`; metal avg `-0.0186` n `18`; unknown avg `0.0262` n `358`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0058` n `228`; crypto_major avg `-0.2877` n `8`; equity avg `-0.2934` n `65`; fx avg `0.0654` n `4`; index avg `-0.0449` n `23`; metal avg `-0.0827` n `18`; unknown avg `0.3496` n `358`
- 4h: commodity avg `-0.748` n `12`; crypto_alt avg `1.3256` n `228`; crypto_major avg `0.7635` n `8`; equity avg `0.3311` n `65`; fx avg `0.0068` n `4`; index avg `0.2075` n `23`; metal avg `1.1945` n `18`; unknown avg `0.5984` n `356`
- 24h: commodity avg `-1.9853` n `7`; crypto_alt avg `0.6421` n `223`; crypto_major avg `-1.2045` n `7`; equity avg `1.1355` n `47`; fx avg `0.0624` n `4`; index avg `1.585` n `6`; metal avg `2.2391` n `7`; unknown avg `1.1696` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `531`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1246`, n `531`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1013`, n `531`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0855`, n `527`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0789`, n `527`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `527`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0776`, n `527`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.074`, n `527`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `527`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0642`, n `531`, weak_sample_signal
