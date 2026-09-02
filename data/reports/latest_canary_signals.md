# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T11:37:27.845357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3197` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0404` n `12`; crypto_alt avg `0.2865` n `232`; crypto_major avg `0.2984` n `8`; equity avg `0.1334` n `132`; fx avg `-0.0134` n `6`; index avg `0.0398` n `26`; metal avg `0.0672` n `20`; unknown avg `0.0842` n `792`
- 1h: commodity avg `-0.2208` n `12`; crypto_alt avg `0.1577` n `232`; crypto_major avg `0.1584` n `8`; equity avg `0.2994` n `132`; fx avg `-0.0463` n `6`; index avg `0.1001` n `26`; metal avg `0.256` n `20`; unknown avg `0.6575` n `790`
- 4h: commodity avg `-0.1822` n `12`; crypto_alt avg `-1.2611` n `232`; crypto_major avg `-1.3504` n `8`; equity avg `-0.4644` n `132`; fx avg `-0.0799` n `6`; index avg `-0.0307` n `26`; metal avg `0.0868` n `20`; unknown avg `0.2931` n `790`
- 24h: commodity avg `0.4895` n `12`; crypto_alt avg `-1.5684` n `232`; crypto_major avg `-2.4983` n `8`; equity avg `-1.5499` n `130`; fx avg `-0.2768` n `6`; index avg `-0.2154` n `26`; metal avg `-0.2697` n `20`; unknown avg `0.0222` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
