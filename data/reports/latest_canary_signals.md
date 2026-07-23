# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T19:09:24.364932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0803` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `-0.0301` n `8`; equity avg `-0.2817` n `100`; fx avg `-0.0012` n `6`; index avg `-0.0296` n `25`; metal avg `-0.0285` n `20`; unknown avg `-0.0206` n `772`
- 1h: commodity avg `-0.3409` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `0.081` n `8`; equity avg `-0.2327` n `100`; fx avg `-0.0053` n `6`; index avg `-0.0291` n `25`; metal avg `-0.0054` n `20`; unknown avg `-0.113` n `772`
- 4h: commodity avg `-0.0828` n `12`; crypto_alt avg `-0.5983` n `230`; crypto_major avg `-0.496` n `8`; equity avg `-0.0222` n `100`; fx avg `0.0062` n `6`; index avg `-0.0111` n `25`; metal avg `-0.1286` n `20`; unknown avg `-0.5529` n `772`
- 24h: commodity avg `0.7416` n `12`; crypto_alt avg `-1.4895` n `230`; crypto_major avg `-2.0816` n `8`; equity avg `-1.5011` n `99`; fx avg `-0.0845` n `6`; index avg `-0.3813` n `25`; metal avg `-0.8397` n `20`; unknown avg `-0.4397` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
