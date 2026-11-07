# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T02:52:22.573007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0294` n `13`; crypto_alt avg `-0.0855` n `239`; crypto_major avg `-0.0721` n `8`; equity avg `-0.1183` n `158`; fx avg `-0.0101` n `6`; index avg `0.0011` n `27`; metal avg `-0.0038` n `20`; unknown avg `1.0189` n `1261`
- 1h: commodity avg `0.0201` n `13`; crypto_alt avg `-0.3092` n `239`; crypto_major avg `-0.1921` n `8`; equity avg `-0.301` n `158`; fx avg `-0.0042` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.8434` n `1255`
- 4h: commodity avg `-0.0285` n `13`; crypto_alt avg `-0.1661` n `239`; crypto_major avg `0.0485` n `8`; equity avg `-0.1331` n `158`; fx avg `-0.0138` n `6`; index avg `0.002` n `27`; metal avg `0.0117` n `20`; unknown avg `0.8895` n `1233`
- 24h: commodity avg `-0.1855` n `13`; crypto_alt avg `0.2509` n `239`; crypto_major avg `-0.4277` n `8`; equity avg `0.1782` n `158`; fx avg `-0.083` n `6`; index avg `0.0306` n `27`; metal avg `0.0021` n `20`; unknown avg `8.8775` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
