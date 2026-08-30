# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T12:52:28.577987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.079` n `231`; crypto_major avg `0.0874` n `8`; equity avg `0.0199` n `128`; fx avg `0.0006` n `6`; index avg `-0.0001` n `26`; metal avg `0.0068` n `20`; unknown avg `0.1066` n `793`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `0.3929` n `231`; crypto_major avg `0.3793` n `8`; equity avg `-0.0172` n `128`; fx avg `-0.001` n `6`; index avg `0.0197` n `26`; metal avg `-0.0061` n `20`; unknown avg `1.309` n `793`
- 4h: commodity avg `-0.0037` n `12`; crypto_alt avg `1.0001` n `231`; crypto_major avg `0.5157` n `8`; equity avg `0.022` n `128`; fx avg `0.0023` n `6`; index avg `0.0269` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.8983` n `789`
- 24h: commodity avg `-0.0303` n `12`; crypto_alt avg `1.8187` n `231`; crypto_major avg `1.2905` n `8`; equity avg `0.3135` n `128`; fx avg `0.0181` n `6`; index avg `0.0851` n `26`; metal avg `0.0835` n `20`; unknown avg `-0.0485` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
