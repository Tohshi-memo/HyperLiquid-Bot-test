# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T14:52:32.950152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `13`; crypto_alt avg `-0.199` n `239`; crypto_major avg `-0.5884` n `8`; equity avg `-0.5434` n `162`; fx avg `0.004` n `6`; index avg `-0.0272` n `27`; metal avg `-0.0331` n `20`; unknown avg `3.5707` n `1266`
- 1h: commodity avg `0.055` n `13`; crypto_alt avg `-0.0794` n `239`; crypto_major avg `-0.1938` n `8`; equity avg `-0.7397` n `162`; fx avg `0.0219` n `6`; index avg `-0.0651` n `27`; metal avg `0.1285` n `20`; unknown avg `4.5937` n `1262`
- 4h: commodity avg `0.1755` n `13`; crypto_alt avg `1.0945` n `239`; crypto_major avg `1.0686` n `8`; equity avg `0.6196` n `162`; fx avg `0.0451` n `6`; index avg `0.014` n `27`; metal avg `0.0524` n `20`; unknown avg `17.6844` n `1218`
- 24h: commodity avg `-0.1603` n `13`; crypto_alt avg `0.2503` n `239`; crypto_major avg `0.2782` n `8`; equity avg `-2.0249` n `162`; fx avg `-0.0463` n `6`; index avg `-0.2368` n `27`; metal avg `-0.1624` n `20`; unknown avg `22.0942` n `1105`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
