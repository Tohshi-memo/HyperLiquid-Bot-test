# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T09:07:30.368049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0677` n `13`; crypto_alt avg `-0.1117` n `235`; crypto_major avg `-0.031` n `8`; equity avg `-0.0923` n `150`; fx avg `-0.0217` n `6`; index avg `-0.0155` n `26`; metal avg `0.0111` n `20`; unknown avg `0.2335` n `1076`
- 1h: commodity avg `-0.0334` n `13`; crypto_alt avg `-0.0641` n `235`; crypto_major avg `-0.1124` n `8`; equity avg `0.0201` n `150`; fx avg `-0.0625` n `6`; index avg `0.003` n `26`; metal avg `-0.0733` n `20`; unknown avg `0.0285` n `1064`
- 4h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.4944` n `235`; crypto_major avg `0.3397` n `8`; equity avg `0.4832` n `150`; fx avg `-0.0018` n `6`; index avg `0.0674` n `26`; metal avg `0.0589` n `20`; unknown avg `0.5595` n `988`
- 24h: commodity avg `-0.391` n `13`; crypto_alt avg `-1.3572` n `235`; crypto_major avg `-1.9933` n `8`; equity avg `-0.4737` n `150`; fx avg `0.0787` n `6`; index avg `0.0549` n `26`; metal avg `0.3886` n `20`; unknown avg `7.3219` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
