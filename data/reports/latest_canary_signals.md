# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T16:22:30.521303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0045` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0527` n `12`; crypto_alt avg `0.1916` n `234`; crypto_major avg `0.2653` n `8`; equity avg `-0.0542` n `141`; fx avg `-0.0033` n `6`; index avg `-0.0042` n `26`; metal avg `0.0185` n `20`; unknown avg `0.4738` n `963`
- 1h: commodity avg `-0.1058` n `12`; crypto_alt avg `-0.3228` n `234`; crypto_major avg `-0.0498` n `8`; equity avg `-0.0303` n `141`; fx avg `-0.0464` n `6`; index avg `0.0163` n `26`; metal avg `-0.0041` n `20`; unknown avg `1.3808` n `955`
- 4h: commodity avg `-0.179` n `12`; crypto_alt avg `-1.0895` n `234`; crypto_major avg `-1.1024` n `8`; equity avg `-0.027` n `141`; fx avg `-0.0407` n `6`; index avg `-0.0979` n `26`; metal avg `-0.138` n `20`; unknown avg `226.0314` n `893`
- 24h: commodity avg `-0.5389` n `12`; crypto_alt avg `0.7538` n `234`; crypto_major avg `-0.7063` n `8`; equity avg `0.4836` n `141`; fx avg `-0.162` n `6`; index avg `-0.0406` n `26`; metal avg `-0.1672` n `20`; unknown avg `2.9095` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
