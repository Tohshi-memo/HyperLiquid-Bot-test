# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T18:37:41.637534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.5705` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2955` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.368` n `239`; crypto_major avg `-0.3516` n `8`; equity avg `-0.4146` n `168`; fx avg `-0.0017` n `6`; index avg `-0.0239` n `27`; metal avg `-0.0845` n `20`; unknown avg `-0.0302` n `1252`
- 1h: commodity avg `-0.0063` n `13`; crypto_alt avg `0.0546` n `239`; crypto_major avg `-0.0553` n `8`; equity avg `0.4421` n `168`; fx avg `-0.0116` n `6`; index avg `0.0378` n `27`; metal avg `0.031` n `20`; unknown avg `0.0984` n `1244`
- 4h: commodity avg `-0.2282` n `13`; crypto_alt avg `-0.8478` n `239`; crypto_major avg `-1.1202` n `8`; equity avg `1.4503` n `168`; fx avg `-0.0647` n `6`; index avg `0.1753` n `27`; metal avg `-0.0219` n `20`; unknown avg `1.3039` n `1226`
- 24h: commodity avg `-0.551` n `13`; crypto_alt avg `-0.1314` n `239`; crypto_major avg `0.1405` n `8`; equity avg `3.293` n `168`; fx avg `-0.1586` n `6`; index avg `0.32` n `27`; metal avg `0.7885` n `20`; unknown avg `50.7568` n `1041`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1301`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0957`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0844`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0811`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0758`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0592`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `669`, weak_sample_signal
