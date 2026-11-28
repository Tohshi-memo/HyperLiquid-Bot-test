# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T06:52:27.407413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `13`; crypto_alt avg `-0.0078` n `239`; crypto_major avg `0.0115` n `8`; equity avg `-0.003` n `168`; fx avg `-0.0111` n `6`; index avg `-0.0059` n `27`; metal avg `0.0138` n `20`; unknown avg `142.778` n `1269`
- 1h: commodity avg `0.0035` n `13`; crypto_alt avg `0.3814` n `239`; crypto_major avg `0.2851` n `8`; equity avg `0.0929` n `168`; fx avg `0.0016` n `6`; index avg `-0.0102` n `27`; metal avg `0.0289` n `20`; unknown avg `0.5362` n `1229`
- 4h: commodity avg `-0.0145` n `13`; crypto_alt avg `-1.2593` n `239`; crypto_major avg `-0.4611` n `8`; equity avg `-0.1661` n `168`; fx avg `0.0147` n `6`; index avg `-0.0388` n `27`; metal avg `-0.0375` n `20`; unknown avg `0.6109` n `1213`
- 24h: commodity avg `-0.7591` n `13`; crypto_alt avg `-2.8843` n `239`; crypto_major avg `-2.3891` n `8`; equity avg `-0.1834` n `168`; fx avg `-0.1312` n `6`; index avg `0.0032` n `27`; metal avg `-0.2059` n `20`; unknown avg `215.7212` n `967`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
