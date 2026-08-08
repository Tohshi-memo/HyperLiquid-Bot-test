# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T21:07:27.821522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.0118` n `230`; crypto_major avg `0.015` n `8`; equity avg `0.0206` n `112`; fx avg `-0.0038` n `6`; index avg `0.007` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0011` n `784`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.0086` n `230`; crypto_major avg `0.0054` n `8`; equity avg `0.0239` n `112`; fx avg `-0.001` n `6`; index avg `0.0113` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.029` n `784`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.0236` n `230`; crypto_major avg `-0.101` n `8`; equity avg `0.187` n `112`; fx avg `0.0014` n `6`; index avg `0.0297` n `25`; metal avg `-0.0145` n `20`; unknown avg `0.3309` n `784`
- 24h: commodity avg `0.131` n `12`; crypto_alt avg `1.6157` n `230`; crypto_major avg `1.3125` n `8`; equity avg `0.6644` n `112`; fx avg `-0.0006` n `6`; index avg `0.0328` n `25`; metal avg `0.0499` n `20`; unknown avg `0.1627` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
