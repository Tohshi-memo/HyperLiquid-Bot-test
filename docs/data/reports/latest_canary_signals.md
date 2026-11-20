# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T04:22:26.569805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0839` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0515` n `13`; crypto_alt avg `-0.0001` n `239`; crypto_major avg `-0.0077` n `8`; equity avg `-0.2044` n `165`; fx avg `-0.0072` n `6`; index avg `-0.0082` n `27`; metal avg `-0.0557` n `20`; unknown avg `-0.0273` n `1260`
- 1h: commodity avg `0.0409` n `13`; crypto_alt avg `-0.6314` n `239`; crypto_major avg `-0.464` n `8`; equity avg `-0.1869` n `165`; fx avg `-0.0088` n `6`; index avg `-0.0629` n `27`; metal avg `0.0061` n `20`; unknown avg `159.5932` n `1252`
- 4h: commodity avg `-0.0482` n `13`; crypto_alt avg `-1.9628` n `239`; crypto_major avg `-1.2877` n `8`; equity avg `-1.2125` n `165`; fx avg `-0.0073` n `6`; index avg `-0.2038` n `27`; metal avg `-0.7711` n `20`; unknown avg `0.3136` n `1250`
- 24h: commodity avg `-0.0453` n `13`; crypto_alt avg `-3.5224` n `239`; crypto_major avg `-2.4051` n `8`; equity avg `-5.9322` n `165`; fx avg `0.0215` n `6`; index avg `-0.5474` n `27`; metal avg `-1.6856` n `20`; unknown avg `5.6337` n `1171`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
