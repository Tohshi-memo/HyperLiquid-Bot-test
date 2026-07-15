# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T18:22:33.705313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.1553` n `230`; crypto_major avg `0.2819` n `8`; equity avg `0.0353` n `94`; fx avg `0.0024` n `6`; index avg `0.0076` n `25`; metal avg `0.1005` n `20`; unknown avg `-0.0334` n `768`
- 1h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.4047` n `230`; crypto_major avg `0.4466` n `8`; equity avg `0.5556` n `94`; fx avg `0.0202` n `6`; index avg `0.1594` n `25`; metal avg `0.3878` n `20`; unknown avg `-0.1002` n `768`
- 4h: commodity avg `0.0284` n `12`; crypto_alt avg `-0.013` n `230`; crypto_major avg `0.0385` n `8`; equity avg `-0.0157` n `94`; fx avg `0.101` n `6`; index avg `0.061` n `25`; metal avg `0.1085` n `20`; unknown avg `-0.0572` n `768`
- 24h: commodity avg `0.0843` n `12`; crypto_alt avg `0.8538` n `230`; crypto_major avg `1.5541` n `8`; equity avg `-0.2861` n `93`; fx avg `0.2188` n `6`; index avg `-0.1565` n `25`; metal avg `0.1436` n `20`; unknown avg `0.3371` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
