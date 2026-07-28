# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T22:22:29.240382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0804` n `12`; crypto_alt avg `-0.038` n `230`; crypto_major avg `-0.0514` n `8`; equity avg `-0.0956` n `102`; fx avg `-0.0044` n `6`; index avg `-0.053` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.01` n `776`
- 1h: commodity avg `0.3811` n `12`; crypto_alt avg `0.0471` n `230`; crypto_major avg `0.1813` n `8`; equity avg `-0.0087` n `102`; fx avg `-0.0092` n `6`; index avg `0.0082` n `25`; metal avg `-0.0437` n `20`; unknown avg `-0.1032` n `776`
- 4h: commodity avg `0.4594` n `12`; crypto_alt avg `0.2831` n `230`; crypto_major avg `0.5395` n `8`; equity avg `1.0076` n `102`; fx avg `0.016` n `6`; index avg `0.031` n `25`; metal avg `-0.0469` n `20`; unknown avg `0.3471` n `775`
- 24h: commodity avg `-0.3877` n `12`; crypto_alt avg `-1.6172` n `230`; crypto_major avg `-0.9997` n `8`; equity avg `-2.5479` n `102`; fx avg `-0.0808` n `6`; index avg `-0.349` n `25`; metal avg `-0.4604` n `20`; unknown avg `0.2081` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
