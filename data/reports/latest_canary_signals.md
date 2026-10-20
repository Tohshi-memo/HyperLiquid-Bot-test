# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T09:22:25.781369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0489` n `13`; crypto_alt avg `0.2334` n `237`; crypto_major avg `0.2173` n `8`; equity avg `0.0773` n `151`; fx avg `0.0119` n `6`; index avg `0.0295` n `26`; metal avg `0.0354` n `20`; unknown avg `0.1343` n `1198`
- 1h: commodity avg `0.1114` n `13`; crypto_alt avg `-0.1497` n `237`; crypto_major avg `0.0101` n `8`; equity avg `-0.2189` n `151`; fx avg `-0.0144` n `6`; index avg `-0.0558` n `26`; metal avg `-0.0054` n `20`; unknown avg `0.4834` n `1196`
- 4h: commodity avg `0.2172` n `13`; crypto_alt avg `-0.5874` n `237`; crypto_major avg `-0.5966` n `8`; equity avg `-0.3323` n `151`; fx avg `-0.0348` n `6`; index avg `-0.0302` n `26`; metal avg `-0.0406` n `20`; unknown avg `6.9839` n `1160`
- 24h: commodity avg `0.3085` n `13`; crypto_alt avg `-0.5703` n `237`; crypto_major avg `-1.203` n `8`; equity avg `-1.7154` n `151`; fx avg `-0.0041` n `6`; index avg `-0.2682` n `26`; metal avg `-0.2287` n `20`; unknown avg `4.5217` n `1041`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
