# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T22:37:33.191190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2346` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.037` n `231`; crypto_major avg `0.0264` n `8`; equity avg `0.0074` n `122`; fx avg `0.0028` n `6`; index avg `0.0032` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.0695` n `795`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `0.4487` n `231`; crypto_major avg `0.3814` n `8`; equity avg `0.1086` n `122`; fx avg `0.0058` n `6`; index avg `0.0066` n `25`; metal avg `0.1005` n `20`; unknown avg `0.0486` n `795`
- 4h: commodity avg `-0.2205` n `12`; crypto_alt avg `-1.3363` n `231`; crypto_major avg `-1.1877` n `8`; equity avg `0.1341` n `122`; fx avg `-0.0049` n `6`; index avg `0.0469` n `25`; metal avg `0.1348` n `20`; unknown avg `-0.3178` n `795`
- 24h: commodity avg `-0.7236` n `12`; crypto_alt avg `-1.771` n `231`; crypto_major avg `-0.6768` n `8`; equity avg `2.0938` n `122`; fx avg `0.0581` n `6`; index avg `0.2595` n `25`; metal avg `-0.036` n `20`; unknown avg `-0.4022` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
