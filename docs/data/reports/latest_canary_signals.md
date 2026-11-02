# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T13:22:28.583124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `13`; crypto_alt avg `-0.1665` n `238`; crypto_major avg `-0.1759` n `8`; equity avg `-0.2164` n `156`; fx avg `-0.0008` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0379` n `20`; unknown avg `18.9833` n `1265`
- 1h: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.6159` n `238`; crypto_major avg `-0.5689` n `8`; equity avg `-0.7955` n `156`; fx avg `0.0081` n `6`; index avg `-0.04` n `27`; metal avg `-0.0843` n `20`; unknown avg `34.5937` n `1259`
- 4h: commodity avg `0.0639` n `13`; crypto_alt avg `-0.4979` n `238`; crypto_major avg `-0.6983` n `8`; equity avg `-0.8883` n `156`; fx avg `-0.0122` n `6`; index avg `-0.065` n `27`; metal avg `-0.1093` n `20`; unknown avg `5.9094` n `1254`
- 24h: commodity avg `-0.488` n `13`; crypto_alt avg `-2.6188` n `238`; crypto_major avg `-0.9103` n `8`; equity avg `0.0505` n `156`; fx avg `0.2939` n `6`; index avg `0.2427` n `27`; metal avg `-0.0583` n `20`; unknown avg `6.9237` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
