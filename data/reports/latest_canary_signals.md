# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T04:22:31.418117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5595` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1239` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `-0.7839` n `235`; crypto_major avg `-0.7231` n `8`; equity avg `-0.0951` n `150`; fx avg `0.0003` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0414` n `20`; unknown avg `1.9718` n `1077`
- 1h: commodity avg `0.0241` n `13`; crypto_alt avg `-0.8839` n `235`; crypto_major avg `-0.8415` n `8`; equity avg `-0.2909` n `150`; fx avg `-0.0145` n `6`; index avg `-0.0412` n `26`; metal avg `-0.019` n `20`; unknown avg `2.2563` n `1069`
- 4h: commodity avg `0.2368` n `13`; crypto_alt avg `-1.3543` n `235`; crypto_major avg `-1.2325` n `8`; equity avg `-0.7792` n `150`; fx avg `0.0485` n `6`; index avg `-0.1086` n `26`; metal avg `0.327` n `20`; unknown avg `1.4561` n `1069`
- 24h: commodity avg `0.4442` n `13`; crypto_alt avg `-1.3131` n `235`; crypto_major avg `-2.3101` n `8`; equity avg `-1.587` n `150`; fx avg `-0.1358` n `6`; index avg `-0.272` n `26`; metal avg `-0.2216` n `20`; unknown avg `247.1336` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
