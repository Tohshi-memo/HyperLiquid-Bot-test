# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T06:52:18.342098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1611` n `228`; crypto_major avg `-0.0387` n `8`; equity avg `-0.0592` n `67`; fx avg `0.0` n `6`; index avg `0.0344` n `23`; metal avg `0.006` n `18`; unknown avg `-0.042` n `386`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.3131` n `228`; crypto_major avg `-0.2381` n `8`; equity avg `0.0075` n `67`; fx avg `-0.0001` n `6`; index avg `0.0007` n `23`; metal avg `0.0357` n `18`; unknown avg `-0.0766` n `376`
- 4h: commodity avg `0.1722` n `12`; crypto_alt avg `-0.6733` n `228`; crypto_major avg `-0.3879` n `8`; equity avg `-0.0859` n `67`; fx avg `0.0078` n `6`; index avg `-0.0518` n `23`; metal avg `0.0196` n `18`; unknown avg `-0.3704` n `376`
- 24h: commodity avg `-0.247` n `12`; crypto_alt avg `-4.0658` n `228`; crypto_major avg `-2.5886` n `8`; equity avg `-2.0009` n `67`; fx avg `0.0541` n `6`; index avg `-0.1973` n `23`; metal avg `-0.7428` n `18`; unknown avg `-2.1547` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
