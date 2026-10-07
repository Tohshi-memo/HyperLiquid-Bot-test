# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T05:07:38.026468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8463` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0068` n `13`; crypto_alt avg `0.1805` n `235`; crypto_major avg `0.1666` n `8`; equity avg `-0.017` n `150`; fx avg `-0.0032` n `6`; index avg `0.0011` n `26`; metal avg `-0.0275` n `20`; unknown avg `0.103` n `1074`
- 1h: commodity avg `-0.0063` n `13`; crypto_alt avg `0.0571` n `235`; crypto_major avg `0.1195` n `8`; equity avg `-0.049` n `150`; fx avg `-0.0215` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0511` n `20`; unknown avg `-0.1282` n `1074`
- 4h: commodity avg `0.0581` n `13`; crypto_alt avg `-3.1295` n `235`; crypto_major avg `-1.9167` n `8`; equity avg `-0.5358` n `150`; fx avg `-0.0367` n `6`; index avg `-0.0704` n `26`; metal avg `-0.1699` n `20`; unknown avg `1.7332` n `1068`
- 24h: commodity avg `0.4753` n `13`; crypto_alt avg `-3.4491` n `235`; crypto_major avg `-2.4773` n `8`; equity avg `-0.0831` n `149`; fx avg `0.0391` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0419` n `20`; unknown avg `871.3398` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1874`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
