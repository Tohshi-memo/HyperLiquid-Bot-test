# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T17:37:25.862210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `12`; crypto_alt avg `0.0511` n `230`; crypto_major avg `0.0763` n `8`; equity avg `0.0884` n `112`; fx avg `-0.0008` n `6`; index avg `0.0053` n `25`; metal avg `0.0051` n `20`; unknown avg `-0.0631` n `784`
- 1h: commodity avg `0.1334` n `12`; crypto_alt avg `0.0438` n `230`; crypto_major avg `0.1998` n `8`; equity avg `0.1664` n `112`; fx avg `-0.0` n `6`; index avg `0.0107` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0477` n `784`
- 4h: commodity avg `0.0434` n `12`; crypto_alt avg `0.9414` n `230`; crypto_major avg `0.7687` n `8`; equity avg `0.2386` n `112`; fx avg `-0.0023` n `6`; index avg `0.0087` n `25`; metal avg `0.0122` n `20`; unknown avg `0.0304` n `784`
- 24h: commodity avg `-0.0656` n `12`; crypto_alt avg `1.7561` n `230`; crypto_major avg `2.0407` n `8`; equity avg `0.9945` n `112`; fx avg `0.0216` n `6`; index avg `0.0804` n `25`; metal avg `0.1544` n `20`; unknown avg `0.1555` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
