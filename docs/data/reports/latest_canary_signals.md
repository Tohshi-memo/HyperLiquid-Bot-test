# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T07:37:32.375992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1099` n `13`; crypto_alt avg `-0.0754` n `235`; crypto_major avg `-0.1443` n `8`; equity avg `-0.0172` n `151`; fx avg `0.0033` n `6`; index avg `0.0047` n `26`; metal avg `0.0562` n `20`; unknown avg `0.281` n `1133`
- 1h: commodity avg `-0.169` n `13`; crypto_alt avg `-0.0928` n `235`; crypto_major avg `0.0835` n `8`; equity avg `0.0198` n `151`; fx avg `-0.0226` n `6`; index avg `0.0281` n `26`; metal avg `0.0717` n `20`; unknown avg `0.0854` n `1131`
- 4h: commodity avg `0.0693` n `13`; crypto_alt avg `0.1228` n `235`; crypto_major avg `0.5352` n `8`; equity avg `-0.3424` n `151`; fx avg `0.0058` n `6`; index avg `-0.0615` n `26`; metal avg `-0.0298` n `20`; unknown avg `0.6456` n `1043`
- 24h: commodity avg `-0.4108` n `13`; crypto_alt avg `2.4993` n `235`; crypto_major avg `1.9389` n `8`; equity avg `-0.5383` n `151`; fx avg `-0.0751` n `6`; index avg `-0.041` n `26`; metal avg `0.1089` n `20`; unknown avg `0.3986` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
