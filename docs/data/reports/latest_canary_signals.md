# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T16:07:29.842781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `12`; crypto_alt avg `0.1622` n `230`; crypto_major avg `-0.0271` n `8`; equity avg `0.1499` n `114`; fx avg `0.0128` n `6`; index avg `0.0213` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0074` n `791`
- 1h: commodity avg `-0.0788` n `12`; crypto_alt avg `0.6139` n `230`; crypto_major avg `0.3226` n `8`; equity avg `-0.2997` n `114`; fx avg `0.0592` n `6`; index avg `-0.0693` n `25`; metal avg `0.0001` n `20`; unknown avg `0.1999` n `791`
- 4h: commodity avg `0.0044` n `12`; crypto_alt avg `0.4731` n `230`; crypto_major avg `0.0881` n `8`; equity avg `-0.8445` n `114`; fx avg `0.1032` n `6`; index avg `-0.169` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.2517` n `786`
- 24h: commodity avg `-0.1326` n `12`; crypto_alt avg `0.1094` n `230`; crypto_major avg `-0.5372` n `8`; equity avg `-0.3307` n `114`; fx avg `0.0975` n `6`; index avg `-0.0698` n `25`; metal avg `0.2322` n `20`; unknown avg `0.4095` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
