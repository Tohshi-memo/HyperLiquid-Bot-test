# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T00:52:17.405566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0436` n `12`; crypto_alt avg `0.2283` n `228`; crypto_major avg `0.215` n `8`; equity avg `0.0748` n `67`; fx avg `-0.0005` n `6`; index avg `-0.0041` n `23`; metal avg `-0.0033` n `18`; unknown avg `0.7235` n `386`
- 1h: commodity avg `0.0846` n `12`; crypto_alt avg `-0.0186` n `228`; crypto_major avg `-0.2834` n `8`; equity avg `-0.3259` n `67`; fx avg `-0.0022` n `6`; index avg `-0.1675` n `23`; metal avg `-0.0608` n `18`; unknown avg `0.3538` n `386`
- 4h: commodity avg `0.7414` n `12`; crypto_alt avg `-1.3672` n `228`; crypto_major avg `-0.8078` n `8`; equity avg `-0.6697` n `67`; fx avg `0.0076` n `6`; index avg `-0.2804` n `23`; metal avg `-0.0818` n `18`; unknown avg `-0.0422` n `386`
- 24h: commodity avg `-0.0529` n `12`; crypto_alt avg `-3.5535` n `228`; crypto_major avg `-2.6583` n `8`; equity avg `-1.8957` n `67`; fx avg `0.1489` n `6`; index avg `-0.09` n `23`; metal avg `-0.8863` n `18`; unknown avg `-1.1137` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
