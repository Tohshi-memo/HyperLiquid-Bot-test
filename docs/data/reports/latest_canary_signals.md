# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T02:22:26.972380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.5059` n `234`; crypto_major avg `-0.226` n `8`; equity avg `0.1436` n `141`; fx avg `-0.0059` n `6`; index avg `0.0149` n `26`; metal avg `0.0356` n `20`; unknown avg `-0.1398` n `963`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `-1.201` n `234`; crypto_major avg `-0.4716` n `8`; equity avg `0.2001` n `141`; fx avg `-0.0018` n `6`; index avg `0.0336` n `26`; metal avg `0.0358` n `20`; unknown avg `-0.0411` n `961`
- 4h: commodity avg `0.0287` n `12`; crypto_alt avg `-1.1782` n `234`; crypto_major avg `-0.6016` n `8`; equity avg `-0.2772` n `141`; fx avg `-0.025` n `6`; index avg `-0.0514` n `26`; metal avg `-0.0416` n `20`; unknown avg `0.0702` n `955`
- 24h: commodity avg `0.0087` n `12`; crypto_alt avg `-4.683` n `234`; crypto_major avg `-2.1781` n `8`; equity avg `-2.1836` n `141`; fx avg `-0.0642` n `6`; index avg `-0.1785` n `26`; metal avg `-0.5902` n `20`; unknown avg `135.1702` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
