# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T12:20:14.243167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4222` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.1627` n `234`; crypto_major avg `-0.2185` n `8`; equity avg `-0.0877` n `140`; fx avg `0.0004` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0133` n `20`; unknown avg `2.639` n `946`
- 1h: commodity avg `0.1198` n `12`; crypto_alt avg `-0.1222` n `234`; crypto_major avg `-0.3497` n `8`; equity avg `-0.269` n `140`; fx avg `-0.014` n `6`; index avg `-0.0452` n `26`; metal avg `0.0277` n `20`; unknown avg `21.8872` n `938`
- 4h: commodity avg `0.2218` n `12`; crypto_alt avg `-1.2373` n `234`; crypto_major avg `-1.5263` n `8`; equity avg `-0.7485` n `140`; fx avg `-0.0133` n `6`; index avg `-0.1041` n `26`; metal avg `-0.14` n `20`; unknown avg `4.615` n `937`
- 24h: commodity avg `0.6924` n `12`; crypto_alt avg `2.6766` n `234`; crypto_major avg `-0.2399` n `8`; equity avg `0.3445` n `140`; fx avg `-0.0129` n `6`; index avg `-0.0011` n `26`; metal avg `-0.2924` n `20`; unknown avg `2.8624` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1554`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
