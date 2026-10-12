# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T16:37:28.517908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `-0.1018` n `235`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0937` n `151`; fx avg `-0.0046` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.2567` n `1134`
- 1h: commodity avg `-0.0718` n `13`; crypto_alt avg `-0.041` n `235`; crypto_major avg `-0.0134` n `8`; equity avg `0.0063` n `151`; fx avg `-0.0229` n `6`; index avg `0.0077` n `26`; metal avg `0.0085` n `20`; unknown avg `0.2676` n `1126`
- 4h: commodity avg `0.3353` n `13`; crypto_alt avg `-1.099` n `235`; crypto_major avg `-0.4417` n `8`; equity avg `-1.5217` n `151`; fx avg `-0.0376` n `6`; index avg `-0.0789` n `26`; metal avg `-0.0284` n `20`; unknown avg `0.3322` n `1074`
- 24h: commodity avg `0.5027` n `13`; crypto_alt avg `-2.4097` n `235`; crypto_major avg `-1.6996` n `8`; equity avg `-3.1984` n `151`; fx avg `-0.1615` n `6`; index avg `-0.2838` n `26`; metal avg `-0.1354` n `20`; unknown avg `-0.4002` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2057`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1832`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1104`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0927`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0896`, n `666`, weak_sample_signal
