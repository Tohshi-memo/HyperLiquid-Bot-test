# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T14:37:24.767128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `-0.0203` n `231`; crypto_major avg `-0.0649` n `8`; equity avg `-0.0168` n `128`; fx avg `0.0098` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.1656` n `793`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.0381` n `231`; crypto_major avg `0.107` n `8`; equity avg `0.0212` n `128`; fx avg `0.0046` n `6`; index avg `-0.0183` n `26`; metal avg `0.0675` n `20`; unknown avg `1.2722` n `793`
- 4h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.6147` n `231`; crypto_major avg `0.8188` n `8`; equity avg `0.0324` n `128`; fx avg `0.0043` n `6`; index avg `0.0101` n `26`; metal avg `0.0776` n `20`; unknown avg `1.0928` n `789`
- 24h: commodity avg `-0.0377` n `12`; crypto_alt avg `1.327` n `231`; crypto_major avg `1.202` n `8`; equity avg `0.3037` n `128`; fx avg `0.0158` n `6`; index avg `0.0774` n `26`; metal avg `0.1556` n `20`; unknown avg `-0.1853` n `730`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
