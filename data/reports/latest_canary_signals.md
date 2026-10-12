# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T15:22:36.809990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0823` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0512` n `13`; crypto_alt avg `0.1264` n `235`; crypto_major avg `0.1035` n `8`; equity avg `-0.0728` n `151`; fx avg `-0.0089` n `6`; index avg `0.0024` n `26`; metal avg `-0.0159` n `20`; unknown avg `0.737` n `1134`
- 1h: commodity avg `0.1019` n `13`; crypto_alt avg `-0.4171` n `235`; crypto_major avg `-0.3289` n `8`; equity avg `-0.3259` n `151`; fx avg `-0.0192` n `6`; index avg `0.0015` n `26`; metal avg `-0.0291` n `20`; unknown avg `0.0135` n `1080`
- 4h: commodity avg `0.4152` n `13`; crypto_alt avg `-1.6546` n `235`; crypto_major avg `-1.2087` n `8`; equity avg `-1.7575` n `151`; fx avg `-0.0009` n `6`; index avg `-0.1264` n `26`; metal avg `-0.1333` n `20`; unknown avg `-0.2918` n `1073`
- 24h: commodity avg `0.5666` n `13`; crypto_alt avg `-1.2772` n `235`; crypto_major avg `-0.6048` n `8`; equity avg `-3.0741` n `151`; fx avg `-0.1334` n `6`; index avg `-0.2895` n `26`; metal avg `-0.1267` n `20`; unknown avg `-0.4437` n `881`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2386`, n `667`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2145`, n `667`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `667`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `667`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1061`, n `667`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `667`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `667`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `667`, weak_sample_signal
