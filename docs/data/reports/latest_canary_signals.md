# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T09:52:29.032504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.2892` n `233`; crypto_major avg `-0.3437` n `8`; equity avg `-0.1928` n `134`; fx avg `0.0019` n `6`; index avg `-0.0431` n `26`; metal avg `-0.0432` n `20`; unknown avg `1.0032` n `798`
- 1h: commodity avg `0.0976` n `12`; crypto_alt avg `-0.7788` n `233`; crypto_major avg `-0.7746` n `8`; equity avg `-0.5661` n `134`; fx avg `-0.0297` n `6`; index avg `-0.1021` n `26`; metal avg `-0.0746` n `20`; unknown avg `0.381` n `796`
- 4h: commodity avg `0.2674` n `12`; crypto_alt avg `0.2778` n `233`; crypto_major avg `0.0594` n `8`; equity avg `-0.275` n `134`; fx avg `-0.0156` n `6`; index avg `-0.1149` n `26`; metal avg `-0.0337` n `20`; unknown avg `0.395` n `772`
- 24h: commodity avg `-0.0188` n `12`; crypto_alt avg `-0.6065` n `232`; crypto_major avg `0.4335` n `8`; equity avg `0.5885` n `134`; fx avg `-0.0818` n `6`; index avg `-0.1009` n `26`; metal avg `-0.1089` n `20`; unknown avg `0.8419` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
