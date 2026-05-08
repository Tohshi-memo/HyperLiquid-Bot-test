# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T05:22:21.549916+00:00`
- Correlation status: `ready`
- Asset price records: `617`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0722` n `12`; crypto_alt avg `-0.0835` n `228`; crypto_major avg `0.0213` n `8`; equity avg `0.1559` n `65`; fx avg `-0.0095` n `5`; index avg `0.0197` n `23`; metal avg `0.0859` n `18`; unknown avg `-0.2529` n `365`
- 1h: commodity avg `-0.1246` n `12`; crypto_alt avg `-0.1758` n `228`; crypto_major avg `-0.1573` n `8`; equity avg `0.1685` n `65`; fx avg `-0.0006` n `5`; index avg `0.028` n `23`; metal avg `0.063` n `18`; unknown avg `-0.5073` n `365`
- 4h: commodity avg `-0.049` n `12`; crypto_alt avg `0.3258` n `228`; crypto_major avg `-0.1374` n `8`; equity avg `0.1921` n `65`; fx avg `0.059` n `5`; index avg `0.0666` n `23`; metal avg `0.115` n `18`; unknown avg `-0.746` n `365`
- 24h: commodity avg `0.4679` n `12`; crypto_alt avg `1.282` n `228`; crypto_major avg `-1.5448` n `8`; equity avg `-0.9014` n `65`; fx avg `0.2096` n `5`; index avg `-0.6014` n `23`; metal avg `0.5667` n `18`; unknown avg `-0.2097` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1321`, n `613`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1211`, n `609`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1207`, n `609`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `613`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `613`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `613`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `609`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `609`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0789`, n `609`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `613`, weak_sample_signal
