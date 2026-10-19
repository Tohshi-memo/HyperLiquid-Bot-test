# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T14:07:33.045295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1149` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.4071` n `237`; crypto_major avg `-0.4681` n `8`; equity avg `-0.5619` n `151`; fx avg `0.0059` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0545` n `20`; unknown avg `0.8393` n `1193`
- 1h: commodity avg `-0.0548` n `13`; crypto_alt avg `-0.9356` n `237`; crypto_major avg `-1.0695` n `8`; equity avg `-0.9563` n `151`; fx avg `0.0078` n `6`; index avg `-0.0706` n `26`; metal avg `-0.1242` n `20`; unknown avg `0.6512` n `1193`
- 4h: commodity avg `-0.1794` n `13`; crypto_alt avg `-0.9447` n `237`; crypto_major avg `-1.1564` n `8`; equity avg `-0.539` n `151`; fx avg `0.0362` n `6`; index avg `-0.0415` n `26`; metal avg `-0.2012` n `20`; unknown avg `1.3239` n `1151`
- 24h: commodity avg `-0.3812` n `13`; crypto_alt avg `0.4941` n `237`; crypto_major avg `0.9022` n `8`; equity avg `2.4245` n `151`; fx avg `-0.0177` n `6`; index avg `0.4923` n `26`; metal avg `0.0632` n `20`; unknown avg `1.9006` n `949`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2026`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1546`, n `667`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1382`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0726`, n `667`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0627`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
