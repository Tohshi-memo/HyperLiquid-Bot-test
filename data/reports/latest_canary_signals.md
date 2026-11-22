# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T23:22:28.822640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1852` n `13`; crypto_alt avg `0.0882` n `239`; crypto_major avg `0.0829` n `8`; equity avg `0.4723` n `166`; fx avg `0.0201` n `6`; index avg `0.061` n `27`; metal avg `0.2081` n `20`; unknown avg `0.0872` n `1262`
- 1h: commodity avg `-0.3688` n `13`; crypto_alt avg `0.1267` n `239`; crypto_major avg `0.3037` n `8`; equity avg `0.3635` n `166`; fx avg `0.0225` n `6`; index avg `0.0187` n `27`; metal avg `0.4049` n `20`; unknown avg `202.1119` n `1242`
- 4h: commodity avg `-0.4074` n `13`; crypto_alt avg `-0.1559` n `239`; crypto_major avg `0.2609` n `8`; equity avg `0.2593` n `166`; fx avg `0.1207` n `6`; index avg `-0.012` n `27`; metal avg `0.3672` n `20`; unknown avg `-0.1432` n `1194`
- 24h: commodity avg `-0.5235` n `13`; crypto_alt avg `0.5113` n `239`; crypto_major avg `0.9675` n `8`; equity avg `1.0294` n `166`; fx avg `0.1016` n `6`; index avg `0.0657` n `27`; metal avg `0.4079` n `20`; unknown avg `255.416` n `1034`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
