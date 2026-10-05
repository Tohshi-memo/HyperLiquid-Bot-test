# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T13:52:32.047869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0849` n `13`; crypto_alt avg `0.0666` n `235`; crypto_major avg `0.2932` n `8`; equity avg `-0.1072` n `144`; fx avg `-0.0129` n `6`; index avg `-0.012` n `26`; metal avg `-0.0356` n `20`; unknown avg `0.746` n `1079`
- 1h: commodity avg `-0.1234` n `13`; crypto_alt avg `0.0504` n `235`; crypto_major avg `0.3769` n `8`; equity avg `-0.0997` n `144`; fx avg `-0.0579` n `6`; index avg `0.0534` n `26`; metal avg `-0.0724` n `20`; unknown avg `12.7604` n `1077`
- 4h: commodity avg `-0.1737` n `13`; crypto_alt avg `-0.1573` n `235`; crypto_major avg `0.1386` n `8`; equity avg `-0.1601` n `144`; fx avg `-0.0308` n `6`; index avg `0.0592` n `26`; metal avg `-0.0989` n `20`; unknown avg `4.3183` n `1071`
- 24h: commodity avg `-0.3403` n `13`; crypto_alt avg `0.8407` n `235`; crypto_major avg `1.0468` n `8`; equity avg `-0.1246` n `144`; fx avg `-0.1045` n `6`; index avg `-0.0229` n `26`; metal avg `0.1688` n `20`; unknown avg `-0.6024` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
