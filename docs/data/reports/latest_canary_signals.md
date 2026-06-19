# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T23:07:28.114036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0968` n `12`; crypto_alt avg `-0.0561` n `228`; crypto_major avg `-0.0486` n `8`; equity avg `0.0074` n `78`; fx avg `0.0111` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0053` n `18`; unknown avg `0.0115` n `687`
- 1h: commodity avg `-0.1696` n `12`; crypto_alt avg `0.321` n `228`; crypto_major avg `0.4095` n `8`; equity avg `0.167` n `78`; fx avg `0.051` n `6`; index avg `0.0014` n `23`; metal avg `0.0367` n `18`; unknown avg `-0.2559` n `687`
- 4h: commodity avg `0.0388` n `12`; crypto_alt avg `-0.005` n `228`; crypto_major avg `0.0548` n `8`; equity avg `0.1291` n `78`; fx avg `-0.0078` n `6`; index avg `-0.0139` n `23`; metal avg `0.1786` n `18`; unknown avg `-0.5884` n `687`
- 24h: commodity avg `0.3306` n `12`; crypto_alt avg `-3.6837` n `228`; crypto_major avg `-4.4898` n `8`; equity avg `0.8227` n `78`; fx avg `-0.0852` n `6`; index avg `0.2118` n `23`; metal avg `-4.0792` n `18`; unknown avg `-0.7213` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
