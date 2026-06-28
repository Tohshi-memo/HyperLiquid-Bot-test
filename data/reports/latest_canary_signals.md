# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T06:07:30.438346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.1032` n `228`; crypto_major avg `0.014` n `8`; equity avg `-0.0066` n `88`; fx avg `-0.0022` n `6`; index avg `0.0006` n `23`; metal avg `0.0175` n `20`; unknown avg `-0.0256` n `732`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.2317` n `228`; crypto_major avg `-0.0759` n `8`; equity avg `-0.0132` n `88`; fx avg `-0.0092` n `6`; index avg `0.0099` n `23`; metal avg `0.0032` n `20`; unknown avg `-0.0833` n `732`
- 4h: commodity avg `-0.2349` n `12`; crypto_alt avg `-0.2246` n `228`; crypto_major avg `-0.4857` n `8`; equity avg `-0.0136` n `88`; fx avg `-0.0075` n `6`; index avg `0.0044` n `23`; metal avg `-0.0044` n `20`; unknown avg `15.5177` n `698`
- 24h: commodity avg `0.2591` n `12`; crypto_alt avg `-0.6669` n `228`; crypto_major avg `-1.278` n `8`; equity avg `0.0624` n `88`; fx avg `-0.0239` n `6`; index avg `-0.0964` n `23`; metal avg `-0.0425` n `20`; unknown avg `15.9013` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
