# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T01:52:25.112759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `13`; crypto_alt avg `-0.145` n `238`; crypto_major avg `-0.1359` n `8`; equity avg `-0.2327` n `156`; fx avg `-0.0028` n `6`; index avg `-0.0195` n `27`; metal avg `-0.0186` n `20`; unknown avg `4.0112` n `1259`
- 1h: commodity avg `-0.1285` n `13`; crypto_alt avg `0.256` n `238`; crypto_major avg `0.5207` n `8`; equity avg `0.1344` n `156`; fx avg `-0.0098` n `6`; index avg `-0.0006` n `27`; metal avg `-0.0657` n `20`; unknown avg `0.2956` n `1249`
- 4h: commodity avg `-0.0973` n `13`; crypto_alt avg `0.1337` n `238`; crypto_major avg `0.6372` n `8`; equity avg `0.4712` n `156`; fx avg `0.136` n `6`; index avg `0.198` n `27`; metal avg `0.0669` n `20`; unknown avg `0.0182` n `1219`
- 24h: commodity avg `-0.0729` n `13`; crypto_alt avg `-0.3152` n `238`; crypto_major avg `0.4422` n `8`; equity avg `0.8` n `156`; fx avg `0.1049` n `6`; index avg `0.2649` n `27`; metal avg `0.089` n `20`; unknown avg `1.8041` n `1122`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
