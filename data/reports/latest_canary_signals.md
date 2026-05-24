# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T06:07:18.590907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0482` n `12`; crypto_alt avg `0.0654` n `228`; crypto_major avg `-0.0813` n `8`; equity avg `-0.0193` n `67`; fx avg `-0.004` n `6`; index avg `0.0116` n `23`; metal avg `0.045` n `18`; unknown avg `0.9453` n `386`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `-0.0115` n `228`; crypto_major avg `0.1445` n `8`; equity avg `0.02` n `67`; fx avg `-0.0256` n `6`; index avg `0.0366` n `23`; metal avg `0.0921` n `18`; unknown avg `0.9577` n `386`
- 4h: commodity avg `-0.1786` n `12`; crypto_alt avg `-0.6091` n `228`; crypto_major avg `0.1094` n `8`; equity avg `0.0947` n `67`; fx avg `0.0011` n `6`; index avg `0.0436` n `23`; metal avg `0.1092` n `18`; unknown avg `0.8646` n `386`
- 24h: commodity avg `-3.0679` n `12`; crypto_alt avg `1.9333` n `228`; crypto_major avg `2.6454` n `8`; equity avg `2.392` n `67`; fx avg `0.0376` n `6`; index avg `1.2746` n `23`; metal avg `1.3049` n `18`; unknown avg `1.8635` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
