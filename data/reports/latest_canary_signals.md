# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T02:37:29.312731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.03` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.7155` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2654` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0642` n `13`; crypto_alt avg `-0.3404` n `239`; crypto_major avg `-0.3157` n `8`; equity avg `-0.3803` n `158`; fx avg `0.0032` n `6`; index avg `-0.0816` n `27`; metal avg `-0.0369` n `20`; unknown avg `-0.3006` n `1264`
- 1h: commodity avg `-0.2895` n `13`; crypto_alt avg `-0.3152` n `239`; crypto_major avg `-0.3649` n `8`; equity avg `-0.4663` n `158`; fx avg `-0.0144` n `6`; index avg `-0.1326` n `27`; metal avg `-0.3001` n `20`; unknown avg `-0.297` n `1258`
- 4h: commodity avg `-0.4675` n `13`; crypto_alt avg `-1.698` n `239`; crypto_major avg `-1.8334` n `8`; equity avg `-3.0247` n `158`; fx avg `-0.0287` n `6`; index avg `-0.568` n `27`; metal avg `-0.1179` n `20`; unknown avg `148.268` n `1196`
- 24h: commodity avg `-0.2114` n `13`; crypto_alt avg `-0.3738` n `239`; crypto_major avg `-0.7846` n `8`; equity avg `-1.0987` n `158`; fx avg `0.1217` n `6`; index avg `-0.3853` n `27`; metal avg `-0.4922` n `20`; unknown avg `-0.3099` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
