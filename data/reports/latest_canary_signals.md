# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T01:52:27.540742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8128` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7939` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `-0.0745` n `231`; crypto_major avg `-0.217` n `8`; equity avg `-0.0831` n `128`; fx avg `0.0008` n `6`; index avg `-0.0228` n `26`; metal avg `-0.0228` n `20`; unknown avg `-0.068` n `781`
- 1h: commodity avg `0.2438` n `12`; crypto_alt avg `-0.3307` n `231`; crypto_major avg `-0.5809` n `8`; equity avg `-0.4238` n `128`; fx avg `-0.0561` n `6`; index avg `-0.0738` n `26`; metal avg `-0.2745` n `20`; unknown avg `-0.4509` n `779`
- 4h: commodity avg `-0.1471` n `12`; crypto_alt avg `-1.8374` n `231`; crypto_major avg `-2.1078` n `8`; equity avg `-1.2762` n `128`; fx avg `-0.0481` n `6`; index avg `-0.295` n `26`; metal avg `-0.3139` n `20`; unknown avg `2.8375` n `779`
- 24h: commodity avg `0.3694` n `12`; crypto_alt avg `-0.5296` n `231`; crypto_major avg `-2.1978` n `8`; equity avg `-1.2912` n `128`; fx avg `-0.0268` n `6`; index avg `-0.3002` n `26`; metal avg `-0.3294` n `20`; unknown avg `-0.4692` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
