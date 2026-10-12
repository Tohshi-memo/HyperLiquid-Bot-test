# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T23:07:28.061229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3353` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0721` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `-0.8855` n `235`; crypto_major avg `-0.768` n `8`; equity avg `-0.1811` n `151`; fx avg `-0.0064` n `6`; index avg `-0.0268` n `26`; metal avg `-0.0351` n `20`; unknown avg `2.1611` n `1133`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `-1.4076` n `235`; crypto_major avg `-1.1219` n `8`; equity avg `-0.2802` n `151`; fx avg `-0.0079` n `6`; index avg `-0.0498` n `26`; metal avg `-0.055` n `20`; unknown avg `4.0255` n `1133`
- 4h: commodity avg `-0.0297` n `13`; crypto_alt avg `-1.9895` n `235`; crypto_major avg `-1.3549` n `8`; equity avg `-0.1717` n `151`; fx avg `-0.0108` n `6`; index avg `-0.0196` n `26`; metal avg `0.0348` n `20`; unknown avg `2.886` n `1060`
- 24h: commodity avg `0.2991` n `13`; crypto_alt avg `-5.0965` n `235`; crypto_major avg `-3.3385` n `8`; equity avg `-3.7764` n `151`; fx avg `-0.1581` n `6`; index avg `-0.3773` n `26`; metal avg `-0.0949` n `20`; unknown avg `0.067` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2034`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1774`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0996`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0759`, n `666`, weak_sample_signal
