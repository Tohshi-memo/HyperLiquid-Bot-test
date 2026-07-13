# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T10:37:28.716239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0895` n `12`; crypto_alt avg `0.0919` n `230`; crypto_major avg `0.0502` n `8`; equity avg `-0.0607` n `92`; fx avg `0.0129` n `6`; index avg `-0.046` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0107` n `766`
- 1h: commodity avg `0.2514` n `12`; crypto_alt avg `0.1113` n `230`; crypto_major avg `-0.1627` n `8`; equity avg `-0.1436` n `92`; fx avg `-0.0326` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0469` n `20`; unknown avg `-0.0548` n `766`
- 4h: commodity avg `-0.0958` n `12`; crypto_alt avg `0.4295` n `230`; crypto_major avg `0.1766` n `8`; equity avg `0.5864` n `92`; fx avg `-0.0763` n `6`; index avg `0.085` n `25`; metal avg `0.179` n `20`; unknown avg `-0.0156` n `766`
- 24h: commodity avg `-0.1296` n `12`; crypto_alt avg `-0.859` n `230`; crypto_major avg `-1.0176` n `8`; equity avg `-1.9852` n `92`; fx avg `-0.0718` n `6`; index avg `-0.4529` n `25`; metal avg `-0.212` n `20`; unknown avg `-0.0673` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
