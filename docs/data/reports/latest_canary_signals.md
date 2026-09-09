# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T14:07:31.946231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.1395` n `233`; crypto_major avg `-0.334` n `8`; equity avg `0.199` n `134`; fx avg `-0.0104` n `6`; index avg `0.0707` n `26`; metal avg `0.0715` n `20`; unknown avg `7.414` n `775`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.5415` n `233`; crypto_major avg `-0.5872` n `8`; equity avg `0.631` n `134`; fx avg `0.0033` n `6`; index avg `0.138` n `26`; metal avg `0.2654` n `20`; unknown avg `6.5157` n `773`
- 4h: commodity avg `-0.077` n `12`; crypto_alt avg `0.0718` n `233`; crypto_major avg `0.0293` n `8`; equity avg `0.7614` n `134`; fx avg `0.006` n `6`; index avg `0.13` n `26`; metal avg `0.4851` n `20`; unknown avg `12.8498` n `766`
- 24h: commodity avg `0.1481` n `12`; crypto_alt avg `0.6334` n `232`; crypto_major avg `1.3528` n `8`; equity avg `0.8249` n `134`; fx avg `-0.0916` n `6`; index avg `0.0169` n `26`; metal avg `0.3984` n `20`; unknown avg `6.7795` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
