# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T23:37:24.515377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.1948` n `228`; crypto_major avg `-0.0372` n `8`; equity avg `0.0455` n `74`; fx avg `-0.0037` n `6`; index avg `0.0393` n `23`; metal avg `-0.1099` n `18`; unknown avg `0.1825` n `517`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.5348` n `228`; crypto_major avg `-0.1269` n `8`; equity avg `0.2212` n `74`; fx avg `-0.013` n `6`; index avg `0.1261` n `23`; metal avg `-0.0957` n `18`; unknown avg `-0.2083` n `517`
- 4h: commodity avg `-0.084` n `12`; crypto_alt avg `-1.2745` n `228`; crypto_major avg `-0.5179` n `8`; equity avg `0.1472` n `74`; fx avg `-0.0131` n `6`; index avg `0.1969` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.8955` n `517`
- 24h: commodity avg `-0.6264` n `12`; crypto_alt avg `0.5408` n `228`; crypto_major avg `1.2948` n `8`; equity avg `2.1938` n `74`; fx avg `-0.2852` n `6`; index avg `0.9991` n `23`; metal avg `-0.2631` n `18`; unknown avg `-2.9346` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
