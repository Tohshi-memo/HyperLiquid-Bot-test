# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T06:34:50.382809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0468` n `12`; crypto_alt avg `-0.107` n `228`; crypto_major avg `-0.0572` n `8`; equity avg `-0.0166` n `66`; fx avg `-0.0269` n `6`; index avg `-0.05` n `23`; metal avg `-0.107` n `18`; unknown avg `-0.0535` n `384`
- 1h: commodity avg `-0.1814` n `12`; crypto_alt avg `-0.0126` n `228`; crypto_major avg `0.0585` n `8`; equity avg `0.2676` n `66`; fx avg `-0.0308` n `6`; index avg `0.0822` n `23`; metal avg `0.0569` n `18`; unknown avg `-0.1618` n `374`
- 4h: commodity avg `-0.3279` n `12`; crypto_alt avg `0.8648` n `228`; crypto_major avg `0.868` n `8`; equity avg `0.5781` n `66`; fx avg `-0.0179` n `6`; index avg `0.262` n `23`; metal avg `0.6724` n `18`; unknown avg `0.2906` n `374`
- 24h: commodity avg `0.1979` n `12`; crypto_alt avg `-0.3611` n `228`; crypto_major avg `-0.1177` n `8`; equity avg `0.4498` n `66`; fx avg `-0.1832` n `6`; index avg `-0.427` n `23`; metal avg `-1.6607` n `18`; unknown avg `0.1075` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
