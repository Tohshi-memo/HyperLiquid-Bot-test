# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T01:52:24.657671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.36` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.8301` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3258` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.109` n `13`; crypto_alt avg `-0.0452` n `239`; crypto_major avg `-0.052` n `8`; equity avg `0.0089` n `158`; fx avg `-0.0325` n `6`; index avg `-0.0289` n `27`; metal avg `-0.1589` n `20`; unknown avg `-0.0782` n `1264`
- 1h: commodity avg `-0.2394` n `13`; crypto_alt avg `-0.5043` n `239`; crypto_major avg `-0.5284` n `8`; equity avg `-1.3866` n `158`; fx avg `-0.0991` n `6`; index avg `-0.3062` n `27`; metal avg `0.0683` n `20`; unknown avg `0.1876` n `1258`
- 4h: commodity avg `-0.2969` n `13`; crypto_alt avg `-1.6498` n `239`; crypto_major avg `-1.7918` n `8`; equity avg `-2.625` n `158`; fx avg `-0.0698` n `6`; index avg `-0.466` n `27`; metal avg `0.0383` n `20`; unknown avg `169.7789` n `1196`
- 24h: commodity avg `0.0271` n `13`; crypto_alt avg `-0.2575` n `239`; crypto_major avg `-0.5799` n `8`; equity avg `-0.7021` n `158`; fx avg `0.0557` n `6`; index avg `-0.3045` n `27`; metal avg `-0.4417` n `20`; unknown avg `-0.1829` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
